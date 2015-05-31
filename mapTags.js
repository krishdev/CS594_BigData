
function map1() {
      //  emit(this.items[]."rank",this.items[]."award_count"); 
        
        var mime = "";
        this.items.forEach(function (m) {
//        	mime = m.is_answered;
//        	value= m.question_id;
        	
        	if(m.tags != null)
        	{
        	m.tags.forEach(function(n){
        	mime = n;
        	value= m.question_id;
        	emit(mime, value);});
        	}
        //	emit(mime, value);
        	});        
}