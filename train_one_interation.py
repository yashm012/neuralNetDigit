def train_one_iteration(model_inputs, last_cost:float):

      if cost >= last_cost:
          return False, cost
      else:
          model.slope += slope_update
          model.intercept += intercept_update
          return True, cost
