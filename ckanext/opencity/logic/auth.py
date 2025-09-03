import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def opencity_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "opencity_get_sum": opencity_get_sum,
    }
