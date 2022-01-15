class Developer:
    def __init__(self, developer_name: str, address: str, phone: str, nip: str):
        self._developer_name = developer_name
        self._address = address
        self._phone = phone
        self._nip = nip

    def __str__(self):
        return f'Deweloper {self._developer_name} dzialajacy pod adresem {self._address}. ' \
               f'Telefon kontaktowy: {self._phone}. NIP: {self._phone}.'

    @property
    def get_developer_name(self):
        return self._developer_name

    @property
    def get_address(self):
        return self._address

    @property
    def get_phone(self):
        return self._phone

    @property
    def get_nip(self):
        return self._nip
