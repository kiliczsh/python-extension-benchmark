import timeit

class str(str):
    def add_trailing_slash(self):
        if not self.endswith("/"):
            self += "/"
        return self

def add_trailing_slash_regular(url):
    if not url.endswith("/"):
        url += "/"
    return url

def perform_test(num_inputs, num_iterations):
    def performance_test_extended():
        urls = [str("https://www.example.com" * 1000) for _ in range(num_inputs)]
        for url in urls:
            url.add_trailing_slash()

    def performance_test_regular():
        urls = ["https://www.example.com" * 1000 for _ in range(num_inputs)]
        for url in urls:
            add_trailing_slash_regular(url)

    execution_time_extended = timeit.timeit(performance_test_extended, number=num_iterations)

    execution_time_regular = timeit.timeit(performance_test_regular, number=num_iterations)

    print("Number of inputs:", num_inputs)
    print("Number of iterations:", num_iterations)
    print("Execution time for extended method:", execution_time_extended, "seconds")
    print("Execution time for regular function:", execution_time_regular, "seconds")
    print()

inputs_list = [10, 100, 1000]
iterations_list = [100, 1000, 10000]

for num_inputs in inputs_list:
    for num_iterations in iterations_list:
        perform_test(num_inputs, num_iterations)
