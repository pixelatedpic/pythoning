<?php


class Test_calss {

    public $t = "this is a class";


}


class dbconn {

    private $hostname;
    private $username;
    private $password;
    private $dbname;

    protected function connect(){
        $this->hostname = "localhost";
        $this->username = "root";
        $this->password = "vidhuvaru";
        $this->dbname = "demo";

        $conn = new mysqli($this->hostname, $this->username, $this->password, $this->dbname);
        return $conn;
    }
}

class User extends dbconn{

    protected function getAlldata(){
        $sql = "select * from mwsc_ps";
        $result = $this->connect()->query($sql);
        $numrows = $result->num_rows;
        if ($numrows > 0){
            while ($row = $result->fetch_assoc()){
                $data[] = $row;
            }
            return $data;
        }
    }
}

class viewuser extends User{

    public function showAlldata(){
        $data = $this->getAlldata();
        foreach ($data as $datax){
            echo $datax['waterlevel']."<br>";
            //return $datax;
        }
    }
}

// $object = new Test_calss;
// var_dump($object);
// echo $object->t;
