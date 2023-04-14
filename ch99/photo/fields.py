import os
from PIL import Image # pillow
from django.db.models.fields.files import ImageField, ImageFieldFile # 장고 기본 필드


class ThumbnailImageFieldFile(ImageFieldFile): # 파일 시스템에 직접 파일을 쓰고 지우는 작업을 함.
    # 파일명 기준 thumb nail 파일명을 만들어 줌. ex) abc.jpg -> abc.thumb.jpg
    def _add_thumb(s):
        parts = s.split(".")
        parts.insert(-1, "thumb")
        if parts[-1].lower() not in ['jpeg', 'jpg']:
            parts[-1] = 'jpg'
        return ".".join(parts)
    
    # 원본 파일의 경로인 path 속성에 추가해 thumb_path 속성을 만듬.
    @property
    def thumb_path(self):
        return self._add_thumb(self.path)
    
    # 원본 파일의 URL인 url 속성에 추가해 thumb_url 속성을 만듬.
    @property
    def thumb_url(self):
        return self._add_thumb(self.url)
    
    # 파일 시스템에 파일을 저장하고 생성하는 메소드
    def save(self, name, content, save=True):
        super().save(name, content, save) # ImageFieldFile의 save() 메소드 호출 원본 이미지 저장.
        
        img = Image.open(self.path)
        size = (self.field.thumb_width, self.field.thumb_height)
        img.thumbnail(size)
        background = Image.new('RGB', size, (255, 255, 255))
        box = (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
        background.paste(img, box)
        # 최종 합쳐진 이미지를 JPEG 형식으로 파일 시스템의 thumb_path 경로에 저장
        background.save(self.thumb_path, 'JPEG')
    
    # 삭제시 원본, 썸네일 이미지 같이 삭제
    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super().delete(save)

# 이 클래스가 장고 모델 정의에 사용되는 필드 역할을 함.
class ThumbnailImageField(ImageField):
    # 새로운 filefield 클래스를 정의할 때는 그에 상응하는 file 처리 클래스를 attr_class 속성에 지정하는 것이 필수임.
    attr_class = ThumbnailImageFieldFile
    
    # 모델의 필드 정의 시 이미지의 최대 크기로 가로 세로 옵션을 지정
    def __init__(self, verbose_name=None, thumb_width=128, thumb_height=128, **kwargs):
        self.thumb_width, self.thumb_height = thumb_width, thumb_height
        super().__init__(verbose_name, **kwargs) # 부모 ImageField 클래스의 생성자를 호출해 관련 속성들을 초기화