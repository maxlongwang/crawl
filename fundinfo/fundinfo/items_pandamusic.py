import scrapy


class PandaMusicItem(scrapy.Item):
    pwd_id=scrapy.Field()  # 目录id
    stoken=scrapy.Field()  
    fid=scrapy.Field()  
    to_pdir_fid=scrapy.Field()  
    task_id=scrapy.Field()  
    fid_encrypt=scrapy.Field()  
    download_url=scrapy.Field()  
    file_name=scrapy.Field()      
    url=scrapy.Field()   
    url_goto=scrapy.Field()   
    url_redirect=scrapy.Field()   
    fid_token_list=scrapy.Field()   
    url_page=scrapy.Field()  
    
