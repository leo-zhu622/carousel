from otree.api import *
class Constants(BaseConstants):
    name_in_url = 'carousel_choice'
    players_per_group = None
    num_rounds = 1
    choices = ["unacceptable", "neutral", "acceptable"]  # Binary choices for the carousel
    index = 0

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    carousel_item1 = models.StringField(
        choices=Constants.choices,
        widget=widgets.RadioSelectHorizontal)
    carousel_item2 = models.StringField(
        choices = Constants.choices,
        widget = widgets.RadioSelectHorizontal
    )
    carousel_item3 = models.StringField(
        choices = Constants.choices,
        widget = widgets.RadioSelectHorizontal
    )
    

class CarouselChoice(Page):
    form_model = 'player'
    form_fields = ['carousel_item1', 'carousel_item2', 'carousel_item3']
    constant = 0
    @staticmethod
    def vars_for_template(player: Player):
        return dict(choices=Constants.choices)


page_sequence = [CarouselChoice]
