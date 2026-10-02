class DataFileError(Exception):
    pass


class DataReader:
    def __init__(self, codon_read, weights_read):
        self.codon_read = codon_read
        self.weights_read = weights_read

    def read_codon_table(self):
        codon_table = {}


        with open(self.codon_read, "r", encoding="utf-8") as f:
            
            for line in f:
                vivid_line = line.strip()
                if not vivid_line:
                    continue