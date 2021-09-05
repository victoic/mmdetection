# the new config inherits the base configs to highlight the necessary modification
_base_ = './detectors_htc_r50_1x_coco.py'

# 1. dataset settings
dataset_type = 'CocoDataset'
classes = ('pole', 'cuboid', 'flat', 'disk', 'cylinder', 'sphere', 'wedge')
data = dict(
    train=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes))

# 2. model settings
# explicitly over-write all the `num_classes` field from default 80 to 7.
model = dict(
    roi_head=dict(
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 7.
                num_classes=7),
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 7.
                num_classes=7),
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 7.
                num_classes=7)],
    # explicitly over-write all the `num_classes` field from default 80 to 7.
    ))
lr_config = dict(
  policy='step',
)