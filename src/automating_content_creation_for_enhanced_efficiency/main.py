#!/usr/bin/env python
import sys
from automating_content_creation_for_enhanced_efficiency.crew import AutomatingContentCreationForEnhancedEfficiencyCrew
from automating_content_creation_for_enhanced_efficiency.mail_sender import MailSender

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
    }
    crew_output = AutomatingContentCreationForEnhancedEfficiencyCrew().crew().kickoff(inputs=inputs)
    print(crew_output)
    # blog_post_content = crew_output.pydantic.blog_post_content
    #
    # mail_sender = MailSender()
    # from_email = "antoine@corpogames.fr"  # Replace with your sender email
    # to_email = "vdaubry@gmail.com"
    # subject = "[Agentic] Blog Post Proposal"
    # content = blog_post_content
    #
    # try:
    #     # Send the email
    #     response = mail_sender.send_email(from_email, to_email, subject, content)
    #     print(f"Email sent successfully! Status code: {response['status_code']}")
    # except RuntimeError as e:
    #     print(f"Error: {e}")



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        
    }
    try:
        AutomatingContentCreationForEnhancedEfficiencyCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        AutomatingContentCreationForEnhancedEfficiencyCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        
    }
    try:
        AutomatingContentCreationForEnhancedEfficiencyCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
