from django import template

register = template.Library()

def cut(st,subst):
    return st.replace(subst,'')

register.filter('cutstr',cut)