def postCabinet(title, requires_questions, **kwargs):
    print("New cabinet:\n")
    print(f"title: {title}\n requires_questions: {requires_questions}\n")
    if kwargs["question_title"]:
        print(f"question_title: {kwargs["question_title"]}")