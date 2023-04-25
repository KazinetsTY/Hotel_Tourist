from user_role.widgets import PermissionsSelectMultiply as UserRolePermissionsSelectMultiply


class PermissionsSelectMultiply(UserRolePermissionsSelectMultiply):
    groups_permissions = {
        "Номера": ["hotel_room.room"],
        "Пользователи и роли": ["user_role.role", "core.user"]
    }
