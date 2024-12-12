from lxml import etree
import os  
import cx_Oracle

def savedata(data):
    user='eif'
    passwd='oracle'
    dburl='192.168.144.74/eif'
    conn = cx_Oracle.connect(user, passwd, dburl)
    cursor = conn.cursor()
    cursor.executemany(
            'insert into t_func_ip(function_sid,function_eid,ip,port,filename)  values (:1,:2,:3,:4,:5)', data)
    conn.commit()
    cursor.close()
    conn.close()
    

def get_filename():
    # ./test/testfolder/config/bsconfig/base_comps.xml 
    folder_path='./test/testfolder/config/bsconfig/'
    filenames=os.listdir(folder_path)
    for file in filenames:
        # print(file)
        filename=f'{folder_path}{file}'
        # print(filename)
        para_functionid_ip(filename)

def para_functionid_ip(filename):
    tree = etree.parse(filename)
    root = tree.getroot()
    ip=''
    port=''
    data=[]
    filename2=filename.split('/')[-1]

    for item in root:
        # print(item.tag,item.attrib)
        for subitem in item:
            if subitem.tag=='Servers':
                functionrange=subitem.attrib.get('FunctionGroup')
                for item2 in subitem:
                    for item3 in item2:
                        if item3.attrib.get('Name') =='Address':
                            ip=item3.attrib.get('Value')
                
                        if item3.attrib.get('Name') =='Port':
                            port=item3.attrib.get('Value')
                            
                    for func in functionrange.split(';'):
                        func_sip=func.split('-')[0]
                        func_eip=func.split('-')[-1]
                        # print(func_sip,func_eip,ip,port)
                        tup=(func_sip,func_eip,ip,port,filename2)
                        data.append(tup)
                        # print(data)
    savedata(data)                    
                        



    
get_filename()    
# para_functionid_ip('./test/testfolder/config/bsconfig/community.xml')