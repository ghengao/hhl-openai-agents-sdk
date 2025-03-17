from agents import AsyncOpenAI, OpenAIChatCompletionsModel, OpenAIResponsesModel  # type: ignore
import os


def get_gemini(model: str = "gemini-2.0-flash") -> OpenAIChatCompletionsModel:
    return OpenAIChatCompletionsModel(
        model=model,
        openai_client=AsyncOpenAI(
            api_key=os.environ.get("GEMINI_API_KEY", None),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        ),
    )


def get_openai(model: str = "gpt-4o-mini") -> OpenAIChatCompletionsModel:
    return OpenAIChatCompletionsModel(
        model=model,
        openai_client=AsyncOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY", None),
        ),
    )


def get_gemini_response(model: str = "gemini-2.0-flash") -> OpenAIResponsesModel:
    client = AsyncOpenAI(
        api_key=os.environ.get("GEMINI_API_KEY", None),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )

    return OpenAIResponsesModel(
        model=model,
        openai_client=client,
    )
