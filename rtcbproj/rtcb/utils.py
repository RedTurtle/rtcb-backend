# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from graphene import Node


def extract_value_from_input(input, field_id, model_type, model):
    """
    BBB: metodo utilizzato ampiamente nelle mutation per controllare gli ID che
    vengono ricevuti dal front-end.
    """

    settingID = input.get(field_id, None)
    if not settingID:
        return None
    try:
        settingID = int(settingID)
    except ValueError:
        try:
            _type, settingID = Node.from_global_id(settingID)
            assert (
                _type == model_type
            ), u"Expected a {0} object, found {1}".format(model_type, _type)
        except Exception:
            raise Exception(
                u"Received wrong id for querying the db. "
                u"{0}: {1}".format(field_id, settingID)
            )
    try:
        return model.objects.get(id=settingID)
    except ObjectDoesNotExist:
        raise Exception(
            u"Non esiste nessun oggetto con questo id nel database. "
            u"{0}: {1}".format(field_id, settingID)
        )
