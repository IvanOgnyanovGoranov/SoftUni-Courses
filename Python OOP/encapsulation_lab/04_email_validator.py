class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        first_index_found = False
        second_index_found = False

        name = ''
        mail = ''
        domain = ''

        for char in email:
            if char == '@':
                first_index_found = True
                continue
            if char == '.' and not second_index_found:
                second_index_found = True
                continue

            if not first_index_found:
                name += char
            elif second_index_found:
                domain += char
            else:
                mail += char

        if self.__is_domain_valid(domain) and self.__is_mail_valid(mail) and self.__is_name_valid(name):
            return True
        return False


mails = ["gmail", "softuni", "abv"]

domains = ["com", "bg", "net", 'co.uk']

email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.co.uk"))

print(email_validator.validate("georgios@gmail.net"))

print(email_validator.validate("stamatito@abv.net"))

print(email_validator.validate("abv@softuni.bg"))
