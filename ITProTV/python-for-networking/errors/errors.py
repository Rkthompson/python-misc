
def main():
    # print("main ran")
    # file_path = './som-text.txt' #file not found error
    file_path = './some-text.txt'

    try:
        # file = opn(file_path) #NameError
        file = open(file_path)

        lines = file.readlines()
        print(lines)

    except NameError as error:
        print(type(error))
        print("Text is misspelled.")

    except FileNotFoundError as error:
        print(type(error))
        print("File was not located at {}".format(file_path))

    except Exception as error:
        print(type(error))
        print("Error encountered: {}".format(error))

    finally:
        print('Finnally is running')
        file.close()


if __name__ == "__main__":
    main()
