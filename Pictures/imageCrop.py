from PIL import Image
import os

def resize_image(image_path1, image_path2):
    # 打开第一张图片并获取其尺寸
    img1 = Image.open(image_path1)
    width1, height1 = img1.size

    # 打开第二张图片
    img2 = Image.open(image_path2)

    # 检查第二张图片的尺寸是否大于第一张图片
    width2, height2 = img2.size
    print("image1:", width1, height1,"\nimage2:",width2,height2)
    if width2 < width1 or height2 < height1:
        print("implement bicubic interpolation to super-sample.")
        img2 = img2.resize((width1, height1), Image.BICUBIC)

    # 从左上角开始裁剪第二张图片
    img2_resized = img2.crop((0, 0, width1, height1))

    # 保存裁剪后的图片
    base_name, ext = os.path.splitext(image_path2)
    new_image_path = f"{base_name}_resized{ext}"
    img2_resized.save(new_image_path)

    print(f"图片已保存为 {new_image_path}")

# 使用示例
resize_image('./head1.png', './skybox.png')
