class Repository:
    """Converts between models and stored records for one table."""

    def __init__(self, store, table, model_cls):
        # keep all three on self
        self.store = store
        self.table = table
        self.model_cls = model_cls

    def add(self, model):
        """Save a new model and return it with its ID set."""
        record = model.to_dict()
        record.pop(f"{self.table}_id", None)  # Remove the PK if it exists, since insert will set it
        new_id = self.store.insert(self.table, record)
        pk = f"{self.table}_id"
        setattr(model, pk, new_id)  # Set the model's PK to the new ID
        return model


    def list_all(self):
        """Return every stored record as a model."""
        return [self.model_cls.from_dict(record) for record in self.store.get_all(self.table)]


    def get(self, record_id):
        """Return a single stored record as a model."""
        record = self.store.get(self.table, record_id)
        if record is not None:
            return self.model_cls.from_dict(record)
        return None

    def remove(self, record_id):
        """Delete a single stored record."""
        return self.store.delete(self.table, record_id)

    