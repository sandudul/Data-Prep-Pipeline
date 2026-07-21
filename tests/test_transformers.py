from data_processor.transformers import ColumnFilter, MissingValueImputer, TypeCaster

def test_column_filter():
    data = [
        {"a": 1, "b": 2, "c": 3},
        {"a": 4, "b": 5, "c": 6}
    ]
    transformer = ColumnFilter(["a", "c"])
    result = transformer.transform(data)
    assert result == [
        {"a": 1, "c": 3},
        {"a": 4, "c": 6}
    ]


def test_missing_value_imputer():
    data = [
        {"id": 1, "status": "active"},
        {"id": 2, "status": ""},
        {"id": 3, "status": None},
        {"id": 4} # Missing key entirely
    ]
    transformer = MissingValueImputer(column="status", default_value="unknown")
    result = transformer.transform(data)
    assert result == [
        {"id": 1, "status": "active"},
        {"id": 2, "status": "unknown"},
        {"id": 3, "status": "unknown"},
        {"id": 4, "status": "unknown"}
    ]


def test_type_caster():
    data = [
        {"id": "1", "score": "95.5"},
        {"id": "2", "score": "abc"}
    ]
    
    t1 = TypeCaster("id", int)
    t2 = TypeCaster("score", float)
    
    res1 = t1.transform(data)
    assert res1[0]["id"] == 1
    assert res1[1]["id"] == 2
    
    res2 = t2.transform(res1)
    assert res2[0]["score"] == 95.5
    assert res2[1]["score"] == "abc" # Fails to cast, remains unchanged
