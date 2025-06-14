local wall_entities = {}

-- Scan all wall prototypes to catch late-loading mods
for _, entity_type in pairs({"wall", "gate"}) do
	for name, prototype in pairs(data.raw[entity_type] or {}) do
		wall_entities[name] = true

		-- scan all items to find those that place walls or gates
		for item_name, item_prototype in pairs(data.raw["item"] or {}) do
			if item_prototype.place_result and item_prototype.place_result == name then
				item_prototype.place_result = nil

				-- since wall is no longer placeable, it takes it's name from the entity prototype, which does not exist
				-- so we set it's localised_name to replace the one from the wall prototype
				item_prototype.localised_name = {
					"",
					prototype.localised_name or { 'entity-name.' .. name },
				}
				item_prototype.localised_description = {
					"",
					prototype.localised_description or { 'entity-description.' .. name },
				}
				
			end
		end
				-- no item to place this wall/gate
		if prototype.placeable_by then
			prototype.placeable_by = nil
		end

		-- create collision mask that is impossible to place (if not skipped by setting)
		if not settings.startup["no-walls-skip-collision-mask"].value then
			prototype.collision_mask = {layers = {ground_tile = true, water_tile = true}}
			prototype.additional_pastable_entities = {}
		end
	end
end
