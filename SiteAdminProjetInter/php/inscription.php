<?php
include_once '../api_config.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = [
        "id_etudiant" => $_POST['id_etudiant'],
        "nom" => $_POST['nom'],
        "prenom" => $_POST['prenom'],
        "email" => $_POST['email'],
        "mdp" => $_POST['mdp'],
        "departement" => $_POST['departement'],
        "statut" => true
    ];

    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, API_BASE_URL . "etudiants/");
    curl_setopt($curl, CURLOPT_POST, true);
    curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json'
    ]);

    $response = curl_exec($curl);
    $http_code = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    curl_close($curl);

    if ($http_code === 201) {
        $message = "Étudiant ajouté avec succès !";
    } else {
        $message = "Erreur : " . $response;
    }
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ajouter Étudiant</title>
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
    <header>
        <h1>Ajouter un étudiant</h1>
    </header>
    <main>
        <?php if (isset($message)) { echo "<p>$message</p>"; } ?>
        <form action="inscription.php" method="POST">
            <label for="id_etudiant">ID Étudiant :</label>
            <input type="number" id="id_etudiant" name="id_etudiant" required><br><br>

            <label for="nom">Nom :</label>
            <input type="text" id="nom" name="nom" required><br><br>

            <label for="prenom">Prénom :</label>
            <input type="text" id="prenom" name="prenom" required><br><br>

            <label for="email">Email :</label>
            <input type="email" id="email" name="email" required><br><br>

            <label for="mdp">Mot de passe :</label>
            <input type="password" id="mdp" name="mdp" required><br><br>

            <label for="departement">Département :</label>
            <input type="text" id="departement" name="departement"><br><br>

            <button type="submit">Ajouter</button>
        </form>
    </main>
</body>
</html>
