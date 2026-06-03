from pathlib import Path
import gradio as gr
import ollama 

# הגדרת נתיב הפרומפט
PROMPT_PATH = Path("prompts/system_prompt.md")

def load_system_prompt():
    # מוודא שהקובץ קיים לפני קריאה
    if PROMPT_PATH.exists():
        return PROMPT_PATH.read_text(encoding="utf-8")
    return "You are an assistant that converts natural language into Windows CLI commands. Return ONLY the command."

def generate_cli_command(user_input: str) -> str:
    system_prompt = load_system_prompt() 

    try:
        response = ollama.chat(
            model='llama3.1',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_input},
            ]
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.Interface(
    fn=generate_cli_command,
    inputs=gr.Textbox(lines=3, placeholder="Enter a natural language instruction...", label="Human Instruction"),
    outputs=gr.Textbox(label="CLI Command"),
    title="CLI Command Agent",
    description="Convert natural language into Windows CLI commands",
)

if __name__ == "__main__":
    demo.launch()