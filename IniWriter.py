import configparser


class IniWriter():
    ''' Expects section_name as str, filename as str, write_type as str, config_dict as dict '''
    def __init__(self,*args, **kwargs):
        self.section_name = args
        self.filename = args
        self.write_type = args
        self.config_dict = kwargs
        
        write_config = configparser.ConfigParser()  # Pass the imported lib call as a var.
        write_config.add_section(section_name)  # Add a section to our ini file.
        
        for key in config_dict:
            write_config.set(section_name, key, config_dict[key])  # Dynamically set our tuples for the ini.
            
        with open(filename, write_type) as fh:
            write_config.write(fh)  # Write out our ini file.
            

if __name__ == '__main__':
    section_name = 'Main'
    filename = 'test.ini'
    write_type = 'a'
    config_dict = {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
    } 
    IniWriter(section_name, filename, write_type, config_dict)