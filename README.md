# 💻 WinCmd Agent

> A **local** AI agent that converts natural-language instructions into a single Windows CMD command, with built-in safety rules. No API keys, no cloud.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Llama_3.1-111111)
![Gradio](https://img.shields.io/badge/UI-Gradio-FF7C00)

## Example
| You type | Agent returns |
|---|---|
| *"List all files in my Documents folder"* | `dir "%USERPROFILE%\Documents"` |
| *"Create a folder called Reports on the Desktop"* | `mkdir "%USERPROFILE%\Desktop\Reports"` |
| *"Delete everything in System32"* | `UNSAFE_OR_UNCLEAR` |

## ✨ Highlights
- **Runs fully on your machine** with Ollama + Llama 3.1.
- **Strict output contract**: one command, no markdown, no explanations, ready to copy.
- **Safety layer in the system prompt**: requests touching `Windows`, `System32` or drivers, or vague requests like *"fix my computer"*, are refused.
- **Prompt kept in a separate file** (`prompts/system_prompt.md`) so it can be tuned without touching code.
- Simple **Gradio** interface for testing.

## 🚀 Getting started
```bash
ollama pull llama3.1
uv sync          # or: pip install gradio ollama
python main.py
```

## 🧪 Testing
The prompt was refined through repeated test runs; results are tracked in [this sheet](https://docs.google.com/spreadsheets/d/1g9-4UwKkU6cjSOtN7VCjhRP9iNyJu_69Ibuq_aIQc_Y/edit?hl=he&gid=0#gid=0).

> 🔗 Related: **[AI_Engineering](https://github.com/leahlevovitz/AI_Engineering)**, the prompt-engineering lab with 5 versioned prompts for the same task.

---
👩‍💻 Built by **Leah Levovitz** · [LinkedIn](https://www.linkedin.com/in/leahlevovitz) · [GitHub](https://github.com/leahlevovitz)
