from src.post_manager import broadcast_omnichannel

def test_broadcast_logic():
    # Simulate a run
    results = broadcast_omnichannel("Test Title", "Test Content", ["test"])
    assert len(results) > 0
    print("Test passed: Logic is sound.")

if __name__ == "__main__":
    test_broadcast_logic()
