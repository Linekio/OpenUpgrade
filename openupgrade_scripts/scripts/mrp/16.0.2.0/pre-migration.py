from openupgradelib import openupgrade, openupgrade_160

_fields_renames = [
    (
        "mrp.workcenter",
        "mrp_workcenter",
        "capacity",
        "default_capacity",
    ),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(env, _fields_renames)
