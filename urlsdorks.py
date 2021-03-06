#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid
import urlsfile
import urls
import config
import utils
import os
import urllib
#Start of class Scanner

class UrlsDorks:

    
    def start_scan_by_dorks(self,global_vars,scanners,session):

        _utils=utils.Utils()

        if global_vars['goodork_flag']:
            options = _utils.parse_config(config.GOODORK_DIR+"goodork")
            goodork_path=options["path"]
            output_filename=config.GOODORK_DIR+"output/"+str(uuid.uuid4())
            command=goodork_path+" "+global_vars['dorks']+" -o "+output_filename
            print command
            subprocess.call(command.split(),shell=False);
        else:
            output_dir=_utils.create_save_dir(global_vars['save_dir']+"urls")
            output_filename=output_dir+str(uuid.uuid4())
            dork=urllib.pathname2url(global_vars['dorks'])
            if global_vars["advanced_search_url"]:
                if global_vars['dorks'] or global_vars['dorks_file']:
                    advanced_search_url=global_vars["advanced_search_url"].replace("[TEXT]","inurl:"+dork)
            
                u=urls.UrlGoogle('',advanced_search_url)
            elif global_vars['dorks_country']:
                output_filename=output_dir+str(global_vars['dorks']+'_urls.'+global_vars['dorks_country'])
                u=urls.UrlGoogle('site:.'+global_vars['dorks_country']+' inurl:'+dork)
            else:
                u=urls.UrlGoogle(dork) 
            if u.search():
                print 'Scanning...'
                        
                u.save(output_filename,output_dir,global_vars['db_file'])
                if os.path.isfile(output_filename):
##                    if not global_vars['tflag']:
##                        global_vars['targets_file']=output_filename
##                        _urlsfile=urlsfile.UrlsFile()        
##                        _urlsfile.start_scan_by_file(global_vars,scanners,session)
##                    
                    return output_filename
        return ""


