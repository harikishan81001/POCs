import csv



class File2Json(object):
    """
    Take as input a csv file and output json data
    """
    def __init__(self, file_name, *args, **kwargs):
        super(File2Json, self).__init__(*args, **kwargs)
        self.file_name = file_name
        self.file_extn = file_name.split('.')[-1]
        if self.file_extn == 'csv':
            self.converter = self.csv_converter
        else:
            raise InvalidFileFormat("Invalid file format.")

    def process_extra_fields(self, out_dict):
        for data in out_dict:
            extra_dict = {}
            for key, value in data.items():
                if key.startswith('#'):
                    extra_dict[key.split('#')[-1]] = value
                    data.pop(key, None)
            if extra_dict:
                data['extra'] = extra_dict
        return out_dict

    def csv_converter(self):
        """
        csv to json converter
        """
        try:
            with open(self.file_name, 'rb') as f:
                reader = csv.reader(f)
                keys = reader.next()
                lines = []

                # encoding the data in ascii and if error comes in case of
                # ordinal characters not in range then encoding
                # is done as punycode which that ignores these
                # type of characters
                for each in reader:
                    line = []

                    # Remove row if all the cells are empty
                    if not any(each):
                        continue

                    for cell in each:
                        try:
                            cell = cell.strip()
                            line.append(cell.encode('ascii', 'ignore'))
                        except UnicodeDecodeError:
                            line.append(cell.encode('punycode'))
                    lines.append(line)
                out_dict = [dict(zip(keys, line)) for line in lines]
                out_dict = self.process_extra_fields(out_dict)
                return out_dict
        except IOError:
            raise IOError("invalid file path, please check")

    def convert(self):
        """
        Call the converter as per the file format
        """
        return self.converter()
