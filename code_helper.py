from transformers import T5Tokenizer, T5ForConditionalGeneration


def code_helper(input_text):
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xxl")
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xxl")

    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    outputs = model.generate(input_ids)
    print(tokenizer.decode(outputs[0]))

    return tokenizer.decode(outputs[0])
