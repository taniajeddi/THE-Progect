class DataFileError(Exception):
    pass


class DataReader:
    def __init__(self, codon_path="data/codon.txt", weights_path="data/weights.txt"):
        self.codon_path = codon_path
        self.weights_path = weights_path

    def read_codon_table(self):
        codon_table = {}


        with open(self.codon_path, "r", encoding="utf-8") as f:
            line_num = 0
            
            for line in f:
                line_num +=1
                clean_line = line.strip()
                
                if not clean_line:
                    continue

                parting = clean_line.split()
                if len(parting) ==2:

                    if len(parting[0]) == 3:
                        codon = parting[0].upper()
                        amino = parting[1]
                        codon_table[codon] = amino
                    else:
                        raise DataFileError(f"Error in codon file {line_num} : The codon length should be 3 chractars.")

                else:
                    raise DataFileError(f"Error in codon file {line_num} : The line structure should consist of two parts: codon, amino asid.")
        return codon_table

    def is_number(self, text_to_check):
        if len(text_to_check) > 0:
            if text_to_check.count('.') <= 1:
                for char in text_to_check:
                    if char.isdigit() or char == '.':
                        continue
                    else:
                        return False

                return True
        return False   

    def read_amino_weights(self):
        weights = {}
        with open(self.weights_path, "r", encoding="utf-8") as file:
            line_num = 0
            for line in file:
                line_num += 1
                clean_line = line.strip()

                if not clean_line:
                    continue

                parting = clean_line.split()

                if len(parting) == 2:
                    amino = parting[0].upper()

                    if self.is_number(parting[1]):
                        weights[amino] = float(parting[1])
                    else:
                        raise DataFileError(f"Error in weights file {line_num} : The weight should be a digit.")
                else:
                    raise DataFileError(f"Error in weight file {line_num} : The line structure should consist of two parts.")
        
        return weights