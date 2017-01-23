from . import models

def getSettingsForms(user, configModel, configForm):
    retList = []
    settings = configModel.objects.filter(user=user)
    for setting in settings:
        retList.append(configForm(instance=setting))
    retList.append(configForm)
    return retList
