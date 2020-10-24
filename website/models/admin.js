var mongoose=require('mongoose');
var bcrypt=require('bcryptjs');
var ObjectId = mongoose.Schema.Types.ObjectId;
var AdminSchema=mongoose.Schema({
    facultyID:
    {
        type:Number,
        index:true,
        unique:true
    },
    department:
    {
        type:String
    },
    name:
    {
        type:String
    },
    mobile:
    {
        type:Number
    },
    email:
    {
        type:String,
       
    },
    password:
    {
        type:String
    },
    gender:
    {
        type:String
    }
});
var Admin =module.exports=mongoose.model('Admin',AdminSchema);

module.exports.createUser=function(newUser,callback){
    bcrypt.genSalt(10, function(err, salt) {
        bcrypt.hash(newUser.password, salt, function(err, hash) {
            // Store hash in your password DB.
            newUser.password=hash;
            newUser.save(callback);
        });
    });
};
module.exports.getUserByUsername=function(username,callback){
    console.log('inside getuser admin');
    var query={email:username};
    Admin.findOne(query,callback);
};

module.exports.comparePassword=function(candidatePassword,hash,callback){
    bcrypt.compare(candidatePassword, hash, function(err, isMatch) {
        // res === true
        console.log('comparepassword');
        if(err) throw err;
        callback(null,isMatch);
    });
};
module.exports.getUserById=function(id,callback){
    console.log('getuserbyid admin');
   // console.log(User.findById(id).collection('users'));
    Admin.findById(id,callback);
};
