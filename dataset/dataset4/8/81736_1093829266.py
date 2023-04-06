
@patch('a.place.to.patch')
def test_a_thing_calls_what_it_should(self, my_mock):
    # Set up logic here
    my_mock.assert_has_calls([
        call(
            ANY,
            Decimal('20')
        ),
        call(
            ANY,
            Decimal('10')
        )
    ])