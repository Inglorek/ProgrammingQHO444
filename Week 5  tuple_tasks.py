def likelihood():
    # Likelihood of each step falling
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)


def run_task1():
    min_likelihood = likelihood()
    print(f"Minimum likelihood of falling: {min_likelihood}%")


if __name__ == "__main__":
    run_task1()

def likelihood_min_max():
    # Likelihood of each step falling
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods), max(likelihoods)
def run_task2():
    likelihood_values = likelihood_min_max()

    print(f"Minimum likelihood of falling: {likelihood_values[0]}%")
    print(f"Maximum likelihood of falling: {likelihood_values[1]}%")

if __name__ == "__main__":
    run_task2()

def steps():
    # Store step names and their likelihood of falling
    likelihoods = [
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4)
    ]