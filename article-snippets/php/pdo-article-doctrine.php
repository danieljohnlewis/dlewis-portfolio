<?php
use Doctrine\Common\Collections\ArrayCollection;

/** Description of Member
 * @Entity
 */
class Member {
    /** 
     * @Id @GeneratedValue 
     * @Column(type="integer") 
     * @var int
     */
    protected $id;
    /** @Column(type="string") 
     *  @var string 
     */
    protected $firstname;
    /** @Column(type="string")
     *  @var string
     */
    protected $surname;
    /** @Column(type="string")
     *  @var string
     */
    protected $email;
     /** Many members have a membership of many groups
     * @ManyToMany(targetEntity="Group")
     * @var Group[]
     **/
    protected $groups;
    
    /**
     * Constructor 
     */
    public function __construct() {
        $this->groups = new ArrayCollection();
        // ...
    }
    
    //  --- Basic getter and setter examples --- //
    /** Gets the (internal) ID of the member
     * @return int 
     */
    public function getId() {
        return $this->id;
    }
    /** Gets the Firstname of the member
     * @return string 
     */
    public function getFirstname() {
        return $this->firstname;
    }
    /** Sets the firstname of the member
     * @param string $firstname 
     */
    public function setFirstname($firstname) {
        $this->firstname = $firstname;
    }
    
    //  --- More complex getter and setter examples --- //
    /** Gets the groups array of the member
     * @return Group[]
     */
    public function getGroups() {
        return $this->groups;
    }
    
    /**  Assigns a group to a member
     * @param Group $group 
     */
    public function assignToGroup(Group $group) {
        $this->groups[] = $group;
    }
    /** Removes a member from a group
     * @param Group $group 
     */
    public function removeFromGroups(Group $group) {
        $this->getGroups()->removeElement($group);
    }
    // ...
}
?>
