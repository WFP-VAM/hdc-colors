# pylint: disable=missing-function-docstring,redefined-outer-name,protected-access
from rich.text import Text
from rich.table import Table
import pytest

from hdc.colors._classes import HDCDiscreteRamp
from hdc.colors.ui import _spawn_title, _table_gen, create_table, create_overview_table


@pytest.fixture
def discrete_ramp(class_input):
    return HDCDiscreteRamp(class_input)


def test__spawn_title():
    title = _spawn_title("FOO")
    assert isinstance(title, Text)
    assert title.plain == "FOO"


def test_create_table(discrete_ramp):
    tbl = create_table("foo", discrete_ramp)
    assert isinstance(tbl, Table)
    assert tbl.title.plain == "foo"
    assert tbl.show_header
    assert tbl.row_count == 3
    assert len(tbl.columns) == 3
    assert [x.header for x in tbl.columns] == ["Value", "Color", "Label"]
    assert tbl.columns[0]._cells == list(map(str, discrete_ramp.vals))
    assert tbl.columns[2]._cells == discrete_ramp.labels


def test_create_overview_table():
    tbl = create_overview_table()
    assert isinstance(tbl, Table)
    assert tbl.title.plain == "HDC Color Ramps"
    assert [x.header for x in tbl.columns] == ["Name", "Category"]


def test__table_gen():
    # pylint: disable=import-outside-toplevel
    from hdc.colors.vegetation import __all__ as rr

    tblgen = _table_gen(".vegetation", rr)
    assert hasattr(tblgen, "__iter__")
    tbls = list(tblgen)
    assert len(tbls) == len(rr)
    tbls = list(_table_gen(".vegetation", rr, tuple(rr[:1])))
    assert len(tbls) == 1
