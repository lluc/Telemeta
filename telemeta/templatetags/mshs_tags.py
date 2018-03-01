from django import template
from telemeta import models

register = template.Library()


@register.filter
def label_domain(domains):
    # Return a composed string which match with every domain

    res = ''
    list_domain = domains.split(',')

    # Make a dictionnary with the domain's list
    dico = dict(models.MediaItem.DOMAINS)

    # compose the string to return
    for domain in list_domain :
        if dico.has_key(domain) :
            # subsitute whith the corresponding label
            label = dico[domain]
            res = res+label+', '

    # remove the last comma
    res = res.rstrip(', ')

    return res

@register.filter
def label_role(roles):
    # Return a composed string which match with every role

    res = ''
    list_role = roles.split(',')

    # Make a dictionnary with the role's list
    dico = dict(models.Authority.ROLES)

    # compose the string to return
    for role in list_role :
        if dico.has_key(role) :
            # subsitute whith the corresponding label
            label = dico[role]
            res = res+label+', '

    # remove the last comma
    res = res.rstrip(', ')

    return res
