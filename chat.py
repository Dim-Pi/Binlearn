

def chat (this,that):

    if this.lmsg == '//End' :
        this.smode(this.lmod)
        that.smode(that.lmod)
        that.send({'body':'%s درو بست' %this.name})
        return '//End'
    else :
        key = [[{"text":'بریم سر کارمون','command':'//End'}]]
        that.send({'body':this.lmsg ,'keyboard':key})

    














