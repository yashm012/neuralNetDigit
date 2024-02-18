def training_loop():
    print("Training beginning...")
    last_cost = math.inf
    continue_loop = True
    while continue_loop:
        continue_loop, last_cost = train_one_iteration(model_inputs = data[""],
                                                    expectedNum = data[""],
                                                    last_cost = last_cost)

    print("Training complete.")
