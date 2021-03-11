import os
from os.path import isfile, join


def main():
    """We test here the program using two files per test. One contain the input
    and has the prefix "test_" and the other contain the output and has the pre-
    fix "s_". We compare the results of the call of the method with the same co-
    mmand as requested and it should be identical to the solution file. We can 
    choose if we want to ignore the spaces and CR when we compare the result 
    with the solution by setting USE_STRIP. The method will run all the test 
    files available in the folder pointed by path_folder
    """

    PROGRAM_NAME_WITH_PARAMS = "program_mongo_db_json.py"
    PATH_FOLDER = "./test_files/"
    PREFIX_TEST_FILE = "test_"
    PREFIX_SOLUTION_FILE = "s_"
    USE_STRIP = True

    all_files_ok = True

    test_files = [f for f in os.listdir(PATH_FOLDER) if isfile(
        join(PATH_FOLDER, f)) and f.startswith(PREFIX_TEST_FILE)]

    for f in test_files:
        # Apply function on the test file
        command_to_execute = "cat {} | python3 {}".format(
            PATH_FOLDER + f, PROGRAM_NAME_WITH_PARAMS)
        output = os.popen(command_to_execute).read()

        # Get the desired output by reading the solution file
        f_solution = PREFIX_SOLUTION_FILE + f[len(PREFIX_TEST_FILE):]
        command_to_execute = "cat {}".format(PATH_FOLDER + f_solution)
        output_solution = os.popen(command_to_execute).read()

        if USE_STRIP:
            output = output.strip()
            output_solution = output_solution.strip()

        print(f, " is", "OK" if output == output_solution 
            else "not OKAY obtained:\n{}\n SHOULD BE:\n{}".format(
            output, output_solution))

        all_files_ok = all_files_ok and output == output_solution

    if all_files_ok:
        print("\n\nALL TESTS PASSED SUCCESSFULLY! CONGRATULATIONS!")


if __name__ == "__main__":
    main()
