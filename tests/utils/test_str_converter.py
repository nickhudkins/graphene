from graphene.utils import to_snake_case, to_camel_case


def test_snake_case():
    assert to_snake_case('snakesOnAPlane') == 'snakes_on_a_plane'
    assert to_snake_case('SnakesOnAPlane') == 'snakes_on_a_plane'
    assert to_snake_case('snakes_on_a_plane') == 'snakes_on_a_plane'
    assert to_snake_case('IPhoneHysteria') == 'i_phone_hysteria'
    assert to_snake_case('iPhoneHysteria') == 'i_phone_hysteria'


def test_camel_case():
    assert to_camel_case('snakes_on_a_plane') == 'snakesOnAPlane'
    assert to_camel_case('i_phone_hysteria') == 'iPhoneHysteria'