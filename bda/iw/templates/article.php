<?php
	include('../model/coBdd.php');
	if (isset($_POST['id']) and !empty($_POST['id']))
	{
        $request = $bdd->prepare("SELECT title, msg, date_msg
                               FROM msg
                              WHERE id_msg = ?");
        $request->execute(array($_POST['id']));
        $msg = $request->fetch();
?>
                                <h2><?php echo $msg['title']?></h2>
                                <p>
                                    <?php echo $msg['msg']; ?>
                                </p>
                                <p>
                                    <?php echo $msg['date_msg']; ?>
                                </p>
<?php
    }
    else
    {
        echo '42, Great Question of Life, the Universe and Everything';
    }
?>
