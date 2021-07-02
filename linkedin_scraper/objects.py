from . import constants as c


class Institution(object):
    institution_name = None
    website = None
    industry = None
    type = None
    headquarters = None
    company_size = None
    founded = None

    def __init__(
        self,
        name=None,
        website=None,
        industry=None,
        type=None,
        headquarters=None,
        company_size=None,
        founded=None,
    ):
        self.name = name
        self.website = website
        self.industry = industry
        self.type = type
        self.headquarters = headquarters
        self.company_size = company_size
        self.founded = founded


class Experience(Institution):
    from_date = None
    to_date = None
    description = None
    position_title = None
    duration = None

    def __init__(
        self,
        from_date=None,
        to_date=None,
        description=None,
        position_title=None,
        duration=None,
        location=None,
        institution_name=None,
    ):
        self.from_date = from_date
        self.to_date = to_date
        self.description = description
        self.position_title = position_title
        self.duration = duration
        self.location = location
        self.institution_name = institution_name

    def __repr__(self):
        return "{position_title} at {company} from {from_date} to {to_date} for {duration} based at {location} " \
               "with description: {description}".format(
            from_date=self.from_date,
            to_date=self.to_date,
            position_title=self.position_title,
            company=self.institution_name,
            duration=self.duration,
            location=self.location,
            description=self.description,
        )


class Education(Institution):
    from_date = None
    to_date = None
    description = None
    degree = None
    field_of_study = None
    activities_societies = None

    def __init__(self, from_date=None, to_date=None, description=None, degree=None, field_of_study=None,
                 activities_societies=None, institution_name=None):
        self.from_date = from_date
        self.to_date = to_date
        self.description = description
        self.degree = degree
        self.field_of_study = field_of_study
        self.activities_societies = activities_societies
        self.institution_name = institution_name

    def __repr__(self):
        return "{degree} in {field_of_study} at {company} from {from_date} to {to_date} and member of {activities_societies}".format(
            from_date=self.from_date,
            to_date=self.to_date,
            degree=self.degree,
            company=self.institution_name,
            field_of_study=self.field_of_study,
            activities_societies=self.activities_societies,
        )


class Scraper(object):
    driver = None

    def is_signed_in(self):
        try:
            self.driver.find_element_by_id(c.VERIFY_LOGIN_ID)
            return True
        except:
            pass
        return False

    def __find_element_by_class_name__(self, class_name):
        try:
            self.driver.find_element_by_class_name(class_name)
            return True
        except:
            pass
        return False

    def __find_element_by_xpath__(self, tag_name):
        try:
            self.driver.find_element_by_xpath(tag_name)
            return True
        except:
            pass
        return False

    def __find_enabled_element_by_xpath__(self, tag_name):
        try:
            elem = self.driver.find_element_by_xpath(tag_name)
            return elem.is_enabled()
        except:
            pass
        return False

    @classmethod
    def __find_first_available_element__(cls, *args):
        for elem in args:
            if elem:
                return elem[0]
