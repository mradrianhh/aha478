import sys # to access command line arguments.

# Feels more natural for remove_rare to be an extension-method, so I extended the dict-class.
class Words(dict):
    def __init__(self, iterable):
        super().__init__(iterable)

    def remove_rare(self, min_occurences: int) -> {}:
        # If you delete keys from the words-dict as you loop through it, you'll get a runtime-error.
        # By making a identical copy, and deleting the values from it, you can return the copy instead, while avoiding the runtime-error.
        result = self.copy()
        for word in self:
            if int(self[word]) < int(min_occurences):
                del result[word] 
        return result

def word_count(filename: str) -> {}:
    words = Words({})

    with open(sys.argv[1], "r") as file:
        for line in file:
            # filter each line and split by whitespace.
            for word in line.replace(".", "").replace(",", "").replace("\n", "").replace("\t", "").split(" "): 
                word.lower()
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
    
    return words

# Entry point. When calling "python wordcount.py [...]", the __name__ meta-variable of wordcount.py gets set to "__main__". 
if __name__ == "__main__":
    if len(sys.argv) == 2: # If only filename is provided.
        words = word_count(sys.argv[1])
        print(words)
    elif len(sys.argv) == 3: # If filename and min_occurences are provided.
        words = word_count(sys.argv[1]).remove_rare(sys.argv[2])
        print(words)
    else:
        print("Please provide a filename, and an optional number for min occurences in that order.")

