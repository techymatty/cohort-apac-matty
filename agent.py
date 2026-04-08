import os
import logging
from dotenv import load_dotenv

import google.cloud.logging
from google.cloud import datastore

from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.tool_context import ToolContext

# -------------------- ENV --------------------

cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()
MODEL = os.getenv("MODEL")

# -------------------- DATABASE --------------------

DB_ID = "cohortdb"
db = datastore.Client(database=DB_ID)

# -------------------- TOOLS --------------------

def save_user_input(tool_context: ToolContext, user_input: str):
    tool_context.state["USER_INPUT"] = user_input
    return "Input saved"


def create_task(tool_context: ToolContext, title: str):
    key = db.key("Task")
    task = datastore.Entity(key=key)

    task.update({
        "title": title,
        "status": "pending"
    })

    db.put(task)

    return f"Task '{title}' created successfully."


def list_tasks(tool_context: ToolContext):
    results = list(db.query(kind="Task").fetch())

    if not results:
        return "No tasks found."

    return "\n".join(
        [f"- {r.get('title')} ({r.get('status')})" for r in results]
    )


def add_note(tool_context: ToolContext, content: str):
    key = db.key("Note")
    note = datastore.Entity(key=key)

    note.update({"content": content})
    db.put(note)

    return "Note saved successfully."


def create_event(tool_context: ToolContext, title: str, date: str):
    key = db.key("Event")
    event = datastore.Entity(key=key)

    event.update({
        "title": title,
        "date": date
    })

    db.put(event)

    return f"Event '{title}' scheduled on {date}."


def list_events(tool_context: ToolContext):
    results = list(db.query(kind="Event").fetch())

    if not results:
        return "No events found."

    return "\n".join(
        [f"- {r.get('title')} on {r.get('date')}" for r in results]
    )


# -------------------- AGENTS --------------------

task_agent = Agent(
    name="task_agent",
    model=MODEL,
    instruction="""
    Use USER_INPUT to manage tasks.

    - Create task → use create_task
    - List tasks → use list_tasks

    USER_INPUT:
    { USER_INPUT }
    """,
    tools=[create_task, list_tasks]
)

notes_agent = Agent(
    name="notes_agent",
    model=MODEL,
    instruction="""
    Use USER_INPUT to manage notes.

    - Save note → use add_note

    USER_INPUT:
    { USER_INPUT }
    """,
    tools=[add_note]
)

calendar_agent = Agent(
    name="calendar_agent",
    model=MODEL,
    instruction="""
    Use USER_INPUT to manage events.

    - Create event → use create_event
    - List events → use list_events

    USER_INPUT:
    { USER_INPUT }
    """,
    tools=[create_event, list_events]
)

planner_agent = Agent(
    name="planner_agent",
    model=MODEL,
    instruction="""
    Analyze USER_INPUT and decide:

    - Tasks → task_agent
    - Notes → notes_agent
    - Events → calendar_agent
    - Multi-step → call multiple

    USER_INPUT:
    { USER_INPUT }
    """,
    sub_agents=[task_agent, notes_agent, calendar_agent]
)

# ✅ FINAL RESPONSE AGENT (NO VARIABLES)

response_agent = Agent(
    name="response_agent",
    model=MODEL,
    instruction="""
    Generate a final response based on what just happened.

    - If something was created → confirm it
    - If listing → show items clearly
    - Be natural and helpful
    - Do NOT use variables like task_output

    Just respond like a human assistant.
    """
)

# -------------------- WORKFLOW --------------------

workflow = SequentialAgent(
    name="productivity_workflow",
    sub_agents=[planner_agent, response_agent]
)

# -------------------- ROOT --------------------

root_agent = Agent(
    name="productivity_assistant",
    model=MODEL,
    instruction="""
    1. Call save_user_input with user message
    2. Then run workflow
    """,
    tools=[save_user_input],
    sub_agents=[workflow]
)