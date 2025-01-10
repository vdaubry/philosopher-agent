from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.send_message import GmailSendMessage


class EmailToolInput(BaseModel):
    to: str = Field(..., description="Email address of the recipient.")
    subject: str = Field(..., description="Subject of the email.")
    body: str = Field(..., description="Body of the email.")

class EmailTool(BaseTool):
    name: str = "email_tool"
    description: str = (
        "A tool to send an email to a specified recipient."
    )
    args_schema: Type[BaseModel] = EmailToolInput

    def _run(self, to: str, subject: str, body: str) -> str:
        gmail = GmailToolkit()
        send_mail = GmailSendMessage(api_resource=gmail.api_resource)
        result = send_mail({
            'to': [to],
            'subject': subject,
            'message': body
        })
        return f"\nEmail sent: {result}\n"
