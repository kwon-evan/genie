from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

template = """질문: {question}

대답: 차근차근 생각해봅시다. {question}에 대한 답을 찾아보세요."""

prompt = PromptTemplate(template=template, input_variables=["question"])

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# Verbose is required to pass to the callback manager

# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path="../KoAlpaca-7B-Quantized/llama.cpp/models/7B/ggml-model-q4_0.bin",
    callback_manager=callback_manager,
    verbose=True,
)

print("Model Loaded")

llm_chain = LLMChain(prompt=prompt, llm=llm)

print("Chain Loaded")

question = "2023년 현재 대한민국의 대통령은 누구인가요?"

output = llm_chain.run(question)

print(output)
