from pydantic import BaseModel, Field

class InputField(BaseModel):
    """简历表单中的一个字段"""
    name: str = Field(description="字段名称")
    value: str = Field(description="字段的值")
    uid: str = Field(description="字段的UID")

class FormField(BaseModel):
    """整个简历表单的字段信息"""
    fields: list[InputField] = Field(description="字段信息列表")