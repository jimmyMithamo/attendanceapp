UPDATE attendance_member SET group_id = (SELECT id FROM attendance_group WHERE name = 'Group 3')
WHERE name IN ('Litali David Kasyamani', 'Nickson Muturi', 'James Murathe Ngigi', 'Clifftone White', 'Ida Gachoki', 'Joy Junias', 'Lorrine Thuo', 'Catherine Gitau', 'Sarah Mbwaya');
